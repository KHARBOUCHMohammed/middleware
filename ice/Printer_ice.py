# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.8
#
# <auto-generated>
#
# Generated from file `Printer.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module Demo
_M_Demo = Ice.openModule('Demo')
__name__ = 'Demo'

if '_t_bytes' not in _M_Demo.__dict__:
    _M_Demo._t_bytes = IcePy.defineSequence('::Demo::bytes', (), IcePy._t_byte)

if '_t_StringSeq' not in _M_Demo.__dict__:
    _M_Demo._t_StringSeq = IcePy.defineSequence('::Demo::StringSeq', (), IcePy._t_string)

_M_Demo._t_Printer = IcePy.defineValue('::Demo::Printer', Ice.Value, -1, (), False, True, None, ())

if 'PrinterPrx' not in _M_Demo.__dict__:
    _M_Demo.PrinterPrx = Ice.createTempClass()
    class PrinterPrx(Ice.ObjectPrx):

        def printString(self, s, context=None):
            return _M_Demo.Printer._op_printString.invoke(self, ((s, ), context))

        def printStringAsync(self, s, context=None):
            return _M_Demo.Printer._op_printString.invokeAsync(self, ((s, ), context))

        def begin_printString(self, s, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_printString.begin(self, ((s, ), _response, _ex, _sent, context))

        def end_printString(self, _r):
            return _M_Demo.Printer._op_printString.end(self, _r)

        def GetNumberOfMusics(self, context=None):
            return _M_Demo.Printer._op_GetNumberOfMusics.invoke(self, ((), context))

        def GetNumberOfMusicsAsync(self, context=None):
            return _M_Demo.Printer._op_GetNumberOfMusics.invokeAsync(self, ((), context))

        def begin_GetNumberOfMusics(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_GetNumberOfMusics.begin(self, ((), _response, _ex, _sent, context))

        def end_GetNumberOfMusics(self, _r):
            return _M_Demo.Printer._op_GetNumberOfMusics.end(self, _r)

        def GetMusiques(self, i, context=None):
            return _M_Demo.Printer._op_GetMusiques.invoke(self, ((i, ), context))

        def GetMusiquesAsync(self, i, context=None):
            return _M_Demo.Printer._op_GetMusiques.invokeAsync(self, ((i, ), context))

        def begin_GetMusiques(self, i, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_GetMusiques.begin(self, ((i, ), _response, _ex, _sent, context))

        def end_GetMusiques(self, _r):
            return _M_Demo.Printer._op_GetMusiques.end(self, _r)

        def SearchTitle(self, title, context=None):
            return _M_Demo.Printer._op_SearchTitle.invoke(self, ((title, ), context))

        def SearchTitleAsync(self, title, context=None):
            return _M_Demo.Printer._op_SearchTitle.invokeAsync(self, ((title, ), context))

        def begin_SearchTitle(self, title, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_SearchTitle.begin(self, ((title, ), _response, _ex, _sent, context))

        def end_SearchTitle(self, _r):
            return _M_Demo.Printer._op_SearchTitle.end(self, _r)

        def SearchArtist(self, artist, context=None):
            return _M_Demo.Printer._op_SearchArtist.invoke(self, ((artist, ), context))

        def SearchArtistAsync(self, artist, context=None):
            return _M_Demo.Printer._op_SearchArtist.invokeAsync(self, ((artist, ), context))

        def begin_SearchArtist(self, artist, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_SearchArtist.begin(self, ((artist, ), _response, _ex, _sent, context))

        def end_SearchArtist(self, _r):
            return _M_Demo.Printer._op_SearchArtist.end(self, _r)

        def AjtMusique(self, offset, partiesMusique, path, titre, artistes, album, context=None):
            return _M_Demo.Printer._op_AjtMusique.invoke(self, ((offset, partiesMusique, path, titre, artistes, album), context))

        def AjtMusiqueAsync(self, offset, partiesMusique, path, titre, artistes, album, context=None):
            return _M_Demo.Printer._op_AjtMusique.invokeAsync(self, ((offset, partiesMusique, path, titre, artistes, album), context))

        def begin_AjtMusique(self, offset, partiesMusique, path, titre, artistes, album, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_AjtMusique.begin(self, ((offset, partiesMusique, path, titre, artistes, album), _response, _ex, _sent, context))

        def end_AjtMusique(self, _r):
            return _M_Demo.Printer._op_AjtMusique.end(self, _r)

        def AjtMusiqueDatabase(self, titre, artistes, album, context=None):
            return _M_Demo.Printer._op_AjtMusiqueDatabase.invoke(self, ((titre, artistes, album), context))

        def AjtMusiqueDatabaseAsync(self, titre, artistes, album, context=None):
            return _M_Demo.Printer._op_AjtMusiqueDatabase.invokeAsync(self, ((titre, artistes, album), context))

        def begin_AjtMusiqueDatabase(self, titre, artistes, album, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_AjtMusiqueDatabase.begin(self, ((titre, artistes, album), _response, _ex, _sent, context))

        def end_AjtMusiqueDatabase(self, _r):
            return _M_Demo.Printer._op_AjtMusiqueDatabase.end(self, _r)

        def ModifMusique(self, musiqueAModifier, nouveauTitre, nouveauxArtistes, nouvelAlbum, context=None):
            return _M_Demo.Printer._op_ModifMusique.invoke(self, ((musiqueAModifier, nouveauTitre, nouveauxArtistes, nouvelAlbum), context))

        def ModifMusiqueAsync(self, musiqueAModifier, nouveauTitre, nouveauxArtistes, nouvelAlbum, context=None):
            return _M_Demo.Printer._op_ModifMusique.invokeAsync(self, ((musiqueAModifier, nouveauTitre, nouveauxArtistes, nouvelAlbum), context))

        def begin_ModifMusique(self, musiqueAModifier, nouveauTitre, nouveauxArtistes, nouvelAlbum, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_ModifMusique.begin(self, ((musiqueAModifier, nouveauTitre, nouveauxArtistes, nouvelAlbum), _response, _ex, _sent, context))

        def end_ModifMusique(self, _r):
            return _M_Demo.Printer._op_ModifMusique.end(self, _r)

        def DeleteMusic(self, name, context=None):
            return _M_Demo.Printer._op_DeleteMusic.invoke(self, ((name, ), context))

        def DeleteMusicAsync(self, name, context=None):
            return _M_Demo.Printer._op_DeleteMusic.invokeAsync(self, ((name, ), context))

        def begin_DeleteMusic(self, name, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_DeleteMusic.begin(self, ((name, ), _response, _ex, _sent, context))

        def end_DeleteMusic(self, _r):
            return _M_Demo.Printer._op_DeleteMusic.end(self, _r)

        def Play(self, music, context=None):
            return _M_Demo.Printer._op_Play.invoke(self, ((music, ), context))

        def PlayAsync(self, music, context=None):
            return _M_Demo.Printer._op_Play.invokeAsync(self, ((music, ), context))

        def begin_Play(self, music, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_Play.begin(self, ((music, ), _response, _ex, _sent, context))

        def end_Play(self, _r):
            return _M_Demo.Printer._op_Play.end(self, _r)

        def Pause(self, context=None):
            return _M_Demo.Printer._op_Pause.invoke(self, ((), context))

        def PauseAsync(self, context=None):
            return _M_Demo.Printer._op_Pause.invokeAsync(self, ((), context))

        def begin_Pause(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_Pause.begin(self, ((), _response, _ex, _sent, context))

        def end_Pause(self, _r):
            return _M_Demo.Printer._op_Pause.end(self, _r)

        def Stop(self, context=None):
            return _M_Demo.Printer._op_Stop.invoke(self, ((), context))

        def StopAsync(self, context=None):
            return _M_Demo.Printer._op_Stop.invokeAsync(self, ((), context))

        def begin_Stop(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_Stop.begin(self, ((), _response, _ex, _sent, context))

        def end_Stop(self, _r):
            return _M_Demo.Printer._op_Stop.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Demo.PrinterPrx.ice_checkedCast(proxy, '::Demo::Printer', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Demo.PrinterPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Demo::Printer'
    _M_Demo._t_PrinterPrx = IcePy.defineProxy('::Demo::Printer', PrinterPrx)

    _M_Demo.PrinterPrx = PrinterPrx
    del PrinterPrx

    _M_Demo.Printer = Ice.createTempClass()
    class Printer(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Demo::Printer', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Demo::Printer'

        @staticmethod
        def ice_staticId():
            return '::Demo::Printer'

        def printString(self, s, current=None):
            raise NotImplementedError("servant method 'printString' not implemented")

        def GetNumberOfMusics(self, current=None):
            raise NotImplementedError("servant method 'GetNumberOfMusics' not implemented")

        def GetMusiques(self, i, current=None):
            raise NotImplementedError("servant method 'GetMusiques' not implemented")

        def SearchTitle(self, title, current=None):
            raise NotImplementedError("servant method 'SearchTitle' not implemented")

        def SearchArtist(self, artist, current=None):
            raise NotImplementedError("servant method 'SearchArtist' not implemented")

        def AjtMusique(self, offset, partiesMusique, path, titre, artistes, album, current=None):
            raise NotImplementedError("servant method 'AjtMusique' not implemented")

        def AjtMusiqueDatabase(self, titre, artistes, album, current=None):
            raise NotImplementedError("servant method 'AjtMusiqueDatabase' not implemented")

        def ModifMusique(self, musiqueAModifier, nouveauTitre, nouveauxArtistes, nouvelAlbum, current=None):
            raise NotImplementedError("servant method 'ModifMusique' not implemented")

        def DeleteMusic(self, name, current=None):
            raise NotImplementedError("servant method 'DeleteMusic' not implemented")

        def Play(self, music, current=None):
            raise NotImplementedError("servant method 'Play' not implemented")

        def Pause(self, current=None):
            raise NotImplementedError("servant method 'Pause' not implemented")

        def Stop(self, current=None):
            raise NotImplementedError("servant method 'Stop' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_PrinterDisp)

        __repr__ = __str__

    _M_Demo._t_PrinterDisp = IcePy.defineClass('::Demo::Printer', Printer, (), None, ())
    Printer._ice_type = _M_Demo._t_PrinterDisp

    Printer._op_printString = IcePy.Operation('printString', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())
    Printer._op_GetNumberOfMusics = IcePy.Operation('GetNumberOfMusics', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_int, False, 0), ())
    Printer._op_GetMusiques = IcePy.Operation('GetMusiques', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), ((), _M_Demo._t_StringSeq, False, 0), ())
    Printer._op_SearchTitle = IcePy.Operation('SearchTitle', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_Demo._t_StringSeq, False, 0), ())
    Printer._op_SearchArtist = IcePy.Operation('SearchArtist', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_Demo._t_StringSeq, False, 0), ())
    Printer._op_AjtMusique = IcePy.Operation('AjtMusique', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), _M_Demo._t_bytes, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), None, ())
    Printer._op_AjtMusiqueDatabase = IcePy.Operation('AjtMusiqueDatabase', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), None, ())
    Printer._op_ModifMusique = IcePy.Operation('ModifMusique', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), None, ())
    Printer._op_DeleteMusic = IcePy.Operation('DeleteMusic', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())
    Printer._op_Play = IcePy.Operation('Play', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_bool, False, 0), ())
    Printer._op_Pause = IcePy.Operation('Pause', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_string, False, 0), ())
    Printer._op_Stop = IcePy.Operation('Stop', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_bool, False, 0), ())

    _M_Demo.Printer = Printer
    del Printer

_M_Demo._t_PrinterFactory = IcePy.defineValue('::Demo::PrinterFactory', Ice.Value, -1, (), False, True, None, ())

if 'PrinterFactoryPrx' not in _M_Demo.__dict__:
    _M_Demo.PrinterFactoryPrx = Ice.createTempClass()
    class PrinterFactoryPrx(Ice.ObjectPrx):

        def createPrinter(self, context=None):
            return _M_Demo.PrinterFactory._op_createPrinter.invoke(self, ((), context))

        def createPrinterAsync(self, context=None):
            return _M_Demo.PrinterFactory._op_createPrinter.invokeAsync(self, ((), context))

        def begin_createPrinter(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.PrinterFactory._op_createPrinter.begin(self, ((), _response, _ex, _sent, context))

        def end_createPrinter(self, _r):
            return _M_Demo.PrinterFactory._op_createPrinter.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Demo.PrinterFactoryPrx.ice_checkedCast(proxy, '::Demo::PrinterFactory', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Demo.PrinterFactoryPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Demo::PrinterFactory'
    _M_Demo._t_PrinterFactoryPrx = IcePy.defineProxy('::Demo::PrinterFactory', PrinterFactoryPrx)

    _M_Demo.PrinterFactoryPrx = PrinterFactoryPrx
    del PrinterFactoryPrx

    _M_Demo.PrinterFactory = Ice.createTempClass()
    class PrinterFactory(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Demo::PrinterFactory', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Demo::PrinterFactory'

        @staticmethod
        def ice_staticId():
            return '::Demo::PrinterFactory'

        def createPrinter(self, current=None):
            raise NotImplementedError("servant method 'createPrinter' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_PrinterFactoryDisp)

        __repr__ = __str__

    _M_Demo._t_PrinterFactoryDisp = IcePy.defineClass('::Demo::PrinterFactory', PrinterFactory, (), None, ())
    PrinterFactory._ice_type = _M_Demo._t_PrinterFactoryDisp

    PrinterFactory._op_createPrinter = IcePy.Operation('createPrinter', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_Demo._t_PrinterPrx, False, 0), ())

    _M_Demo.PrinterFactory = PrinterFactory
    del PrinterFactory

# End of module Demo
